import torch
import matplotlib.pyplot as plt
import nibabel

def plot_central_cuts(img, title=""):
    """
    param image: tensor or np array of shape (CxDxHxW) if t is None
    """
    if isinstance(img, torch.Tensor):
        img = img.numpy()
        if (len(img.shape) > 3):
            img = img[0,:,:,:]
                
    elif isinstance(img, nibabel.nifti1.Nifti1Image):    
        img = img.get_fdata()
   
    print(img.shape)
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(3 * 4, 4))
    axes[0].imshow(img[ img.shape[0] // 2, :, :], cmap='gray')
    axes[1].imshow(img[ :, img.shape[1] // 2, :], cmap='gray')
    axes[2].imshow(img[ :, :, img.shape[2] // 2], cmap='gray')
    axes[1].set_title(title)
    
    plt.show()
